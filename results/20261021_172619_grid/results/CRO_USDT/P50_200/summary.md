# EMA Hourly Continuation — CRO/USDT P50_200

**Symbol:** CRO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.8231 |
| net_win_rate | 0.5265 |
| gross_profit_factor | 1.0998 |
| gross_win_rate | 0.5265 |
| sharpe_ratio | -0.9565 |
| sortino_ratio | -0.2238 |
| max_drawdown | 0.2981 |
| cagr | -0.0989 |
| net_avg_win | 77.0368 |
| net_avg_loss | -104.0734 |
| avg_hold_time_bars | 34.3295 |
| exposure | 0.4120 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

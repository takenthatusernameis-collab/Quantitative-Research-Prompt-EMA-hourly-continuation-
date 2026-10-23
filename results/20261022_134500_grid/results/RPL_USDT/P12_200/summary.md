# EMA Hourly Continuation — RPL/USDT P12_200

**Symbol:** RPL/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.8278 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 1.0238 |
| gross_win_rate | 0.5076 |
| sharpe_ratio | -1.0275 |
| sortino_ratio | -0.2656 |
| max_drawdown | 0.3113 |
| cagr | -0.1182 |
| net_avg_win | 78.7323 |
| net_avg_loss | -95.6893 |
| avg_hold_time_bars | 51.9970 |
| exposure | 0.7789 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

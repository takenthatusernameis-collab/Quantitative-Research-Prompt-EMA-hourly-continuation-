# EMA Hourly Continuation — ONE/USDT P20_200

**Symbol:** ONE/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.8730 |
| net_win_rate | 0.5053 |
| gross_profit_factor | 1.0174 |
| gross_win_rate | 0.5053 |
| sharpe_ratio | -0.7284 |
| sortino_ratio | -0.1747 |
| max_drawdown | 0.2700 |
| cagr | -0.0795 |
| net_avg_win | 90.9592 |
| net_avg_loss | -106.4350 |
| avg_hold_time_bars | 51.4626 |
| exposure | 0.6573 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

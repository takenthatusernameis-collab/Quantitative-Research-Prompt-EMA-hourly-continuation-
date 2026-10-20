# EMA Hourly Continuation — VR/USDT P34_55

**Symbol:** VR/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 962 |
| net_profit_factor | 0.3698 |
| net_win_rate | 0.2900 |
| gross_profit_factor | 0.6768 |
| gross_win_rate | 0.3139 |
| sharpe_ratio | -15.2233 |
| sortino_ratio | -6.9297 |
| max_drawdown | 1.0000 |
| cagr | -0.9839 |
| net_avg_win | 21.0328 |
| net_avg_loss | -23.2326 |
| avg_hold_time_bars | 3.2193 |
| exposure | 0.1408 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

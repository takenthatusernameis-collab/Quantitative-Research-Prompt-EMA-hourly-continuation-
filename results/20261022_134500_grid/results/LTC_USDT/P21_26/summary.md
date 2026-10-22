# EMA Hourly Continuation — LTC/USDT P21_26

**Symbol:** LTC/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1182 |
| net_profit_factor | 0.1190 |
| net_win_rate | 0.2944 |
| gross_profit_factor | 0.7168 |
| gross_win_rate | 0.3841 |
| sharpe_ratio | -17.6997 |
| sortino_ratio | -9.3070 |
| max_drawdown | 1.0000 |
| cagr | -0.9946 |
| net_avg_win | 3.8806 |
| net_avg_loss | -13.6096 |
| avg_hold_time_bars | 1.6235 |
| exposure | 0.0872 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

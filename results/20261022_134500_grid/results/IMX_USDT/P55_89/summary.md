# EMA Hourly Continuation — IMX/USDT P55_89

**Symbol:** IMX/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 686 |
| net_profit_factor | 0.5342 |
| net_win_rate | 0.4723 |
| gross_profit_factor | 0.9248 |
| gross_win_rate | 0.4883 |
| sharpe_ratio | -5.2524 |
| sortino_ratio | -1.9291 |
| max_drawdown | 0.9120 |
| cagr | -0.6144 |
| net_avg_win | 32.1935 |
| net_avg_loss | -53.9415 |
| avg_hold_time_bars | 3.6851 |
| exposure | 0.1144 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

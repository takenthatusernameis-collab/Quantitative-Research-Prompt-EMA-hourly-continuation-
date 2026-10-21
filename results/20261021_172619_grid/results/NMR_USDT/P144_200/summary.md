# EMA Hourly Continuation — NMR/USDT P144_200

**Symbol:** NMR/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 214 |
| net_profit_factor | 0.6109 |
| net_win_rate | 0.4720 |
| gross_profit_factor | 0.8786 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -2.1868 |
| sortino_ratio | -0.4580 |
| max_drawdown | 0.4318 |
| cagr | -0.1896 |
| net_avg_win | 63.7598 |
| net_avg_loss | -93.2820 |
| avg_hold_time_bars | 7.1916 |
| exposure | 0.0700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — DCR/USDT P26_200

**Symbol:** DCR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.6753 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 0.9420 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -2.7952 |
| sortino_ratio | -0.8718 |
| max_drawdown | 0.6774 |
| cagr | -0.3343 |
| net_avg_win | 57.2916 |
| net_avg_loss | -77.8202 |
| avg_hold_time_bars | 23.3984 |
| exposure | 0.5156 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

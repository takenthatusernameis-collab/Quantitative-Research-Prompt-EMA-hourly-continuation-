# EMA Hourly Continuation — STX/USDT P8_20

**Symbol:** STX/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1728 |
| net_profit_factor | 0.4026 |
| net_win_rate | 0.4190 |
| gross_profit_factor | 0.8107 |
| gross_win_rate | 0.4363 |
| sharpe_ratio | -12.7593 |
| sortino_ratio | -7.4859 |
| max_drawdown | 0.9999 |
| cagr | -0.9770 |
| net_avg_win | 9.3082 |
| net_avg_loss | -16.6717 |
| avg_hold_time_bars | 2.7251 |
| exposure | 0.2131 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — CFG/USDT P26_144

**Symbol:** CFG/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.6103 |
| net_win_rate | 0.4489 |
| gross_profit_factor | 0.8143 |
| gross_win_rate | 0.4489 |
| sharpe_ratio | -2.9535 |
| sortino_ratio | -0.8319 |
| max_drawdown | 0.6443 |
| cagr | -0.3252 |
| net_avg_win | 54.5913 |
| net_avg_loss | -72.8611 |
| avg_hold_time_bars | 32.7207 |
| exposure | 0.5964 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — CELO/USDT P8_20

**Symbol:** CELO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1675 |
| net_profit_factor | 0.3004 |
| net_win_rate | 0.4197 |
| gross_profit_factor | 0.6683 |
| gross_win_rate | 0.4496 |
| sharpe_ratio | -12.2869 |
| sortino_ratio | -7.0832 |
| max_drawdown | 0.9999 |
| cagr | -0.9719 |
| net_avg_win | 6.1061 |
| net_avg_loss | -14.7031 |
| avg_hold_time_bars | 3.0382 |
| exposure | 0.2303 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

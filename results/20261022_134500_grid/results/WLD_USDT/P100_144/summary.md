# EMA Hourly Continuation — WLD/USDT P100_144

**Symbol:** WLD/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.6756 |
| net_win_rate | 0.5152 |
| gross_profit_factor | 1.0863 |
| gross_win_rate | 0.5227 |
| sharpe_ratio | -2.4158 |
| sortino_ratio | -0.6827 |
| max_drawdown | 0.5854 |
| cagr | -0.2778 |
| net_avg_win | 57.0093 |
| net_avg_loss | -89.6534 |
| avg_hold_time_bars | 4.8384 |
| exposure | 0.0871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

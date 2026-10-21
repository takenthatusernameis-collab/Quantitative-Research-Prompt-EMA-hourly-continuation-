# EMA Hourly Continuation — YFI/USDT P21_144

**Symbol:** YFI/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.7637 |
| net_win_rate | 0.5068 |
| gross_profit_factor | 1.0257 |
| gross_win_rate | 0.5068 |
| sharpe_ratio | -1.8135 |
| sortino_ratio | -0.5438 |
| max_drawdown | 0.5313 |
| cagr | -0.2217 |
| net_avg_win | 67.9250 |
| net_avg_loss | -91.3983 |
| avg_hold_time_bars | 26.7795 |
| exposure | 0.5332 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

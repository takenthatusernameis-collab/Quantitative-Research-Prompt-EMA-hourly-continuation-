# EMA Hourly Continuation — YFI/USDT P20_144

**Symbol:** YFI/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 538 |
| net_profit_factor | 0.5882 |
| net_win_rate | 0.4888 |
| gross_profit_factor | 1.0066 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -3.8555 |
| sortino_ratio | -1.2442 |
| max_drawdown | 0.8029 |
| cagr | -0.4592 |
| net_avg_win | 42.7820 |
| net_avg_loss | -69.5649 |
| avg_hold_time_bars | 23.2825 |
| exposure | 0.5668 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

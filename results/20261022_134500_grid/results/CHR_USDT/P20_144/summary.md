# EMA Hourly Continuation — CHR/USDT P20_144

**Symbol:** CHR/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.7383 |
| net_win_rate | 0.4896 |
| gross_profit_factor | 0.9797 |
| gross_win_rate | 0.4919 |
| sharpe_ratio | -2.0825 |
| sortino_ratio | -0.6093 |
| max_drawdown | 0.5638 |
| cagr | -0.2509 |
| net_avg_win | 69.1864 |
| net_avg_loss | -89.8815 |
| avg_hold_time_bars | 31.0696 |
| exposure | 0.6060 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

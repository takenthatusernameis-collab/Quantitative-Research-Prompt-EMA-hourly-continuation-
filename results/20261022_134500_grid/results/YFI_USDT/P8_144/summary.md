# EMA Hourly Continuation — YFI/USDT P8_144

**Symbol:** YFI/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.5765 |
| net_win_rate | 0.4816 |
| gross_profit_factor | 0.9435 |
| gross_win_rate | 0.4893 |
| sharpe_ratio | -3.7014 |
| sortino_ratio | -1.1706 |
| max_drawdown | 0.7696 |
| cagr | -0.4372 |
| net_avg_win | 42.0114 |
| net_avg_loss | -67.6903 |
| avg_hold_time_bars | 32.4913 |
| exposure | 0.7572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

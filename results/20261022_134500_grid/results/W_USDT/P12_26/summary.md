# EMA Hourly Continuation — W/USDT P12_26

**Symbol:** W/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1391 |
| net_profit_factor | 0.5227 |
| net_win_rate | 0.4644 |
| gross_profit_factor | 0.9648 |
| gross_win_rate | 0.4809 |
| sharpe_ratio | -8.2047 |
| sortino_ratio | -4.3028 |
| max_drawdown | 0.9951 |
| cagr | -0.8794 |
| net_avg_win | 16.8666 |
| net_avg_loss | -27.9819 |
| avg_hold_time_bars | 3.0798 |
| exposure | 0.1947 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

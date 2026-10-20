# EMA Hourly Continuation — W/USDT P20_89

**Symbol:** W/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 719 |
| net_profit_factor | 0.7336 |
| net_win_rate | 0.5090 |
| gross_profit_factor | 1.0653 |
| gross_win_rate | 0.5160 |
| sharpe_ratio | -2.7155 |
| sortino_ratio | -1.0323 |
| max_drawdown | 0.7397 |
| cagr | -0.3849 |
| net_avg_win | 53.0310 |
| net_avg_loss | -74.9519 |
| avg_hold_time_bars | 11.8595 |
| exposure | 0.3876 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

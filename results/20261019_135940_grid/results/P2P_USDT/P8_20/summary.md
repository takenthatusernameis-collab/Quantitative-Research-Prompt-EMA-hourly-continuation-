# EMA Hourly Continuation — P2P/USDT P8_20

**Symbol:** P2P/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1612 |
| net_profit_factor | 0.3006 |
| net_win_rate | 0.3114 |
| gross_profit_factor | 0.5261 |
| gross_win_rate | 0.3133 |
| sharpe_ratio | -15.2828 |
| sortino_ratio | -8.6488 |
| max_drawdown | 1.0000 |
| cagr | -0.9872 |
| net_avg_win | 8.5612 |
| net_avg_loss | -12.8807 |
| avg_hold_time_bars | 3.4795 |
| exposure | 0.2550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

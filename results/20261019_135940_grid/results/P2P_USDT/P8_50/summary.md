# EMA Hourly Continuation — P2P/USDT P8_50

**Symbol:** P2P/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1072 |
| net_profit_factor | 0.4085 |
| net_win_rate | 0.3778 |
| gross_profit_factor | 0.5791 |
| gross_win_rate | 0.3797 |
| sharpe_ratio | -8.0758 |
| sortino_ratio | -3.6835 |
| max_drawdown | 0.9891 |
| cagr | -0.8343 |
| net_avg_win | 16.8658 |
| net_avg_loss | -25.0692 |
| avg_hold_time_bars | 9.5037 |
| exposure | 0.4631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

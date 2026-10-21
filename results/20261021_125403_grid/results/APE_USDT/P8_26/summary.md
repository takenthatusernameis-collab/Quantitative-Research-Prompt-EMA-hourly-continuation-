# EMA Hourly Continuation — APE/USDT P8_26

**Symbol:** APE/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.6736 |
| net_win_rate | 0.4635 |
| gross_profit_factor | 0.8989 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -3.4898 |
| sortino_ratio | -1.2622 |
| max_drawdown | 0.7815 |
| cagr | -0.4394 |
| net_avg_win | 53.0511 |
| net_avg_loss | -68.0323 |
| avg_hold_time_bars | 6.3577 |
| exposure | 0.1858 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

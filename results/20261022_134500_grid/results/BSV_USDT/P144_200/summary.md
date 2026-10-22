# EMA Hourly Continuation — BSV/USDT P144_200

**Symbol:** BSV/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.3711 |
| net_win_rate | 0.3871 |
| gross_profit_factor | 0.7739 |
| gross_win_rate | 0.4124 |
| sharpe_ratio | -6.7725 |
| sortino_ratio | -2.0121 |
| max_drawdown | 0.9190 |
| cagr | -0.6317 |
| net_avg_win | 32.2584 |
| net_avg_loss | -54.9074 |
| avg_hold_time_bars | 4.6705 |
| exposure | 0.0921 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

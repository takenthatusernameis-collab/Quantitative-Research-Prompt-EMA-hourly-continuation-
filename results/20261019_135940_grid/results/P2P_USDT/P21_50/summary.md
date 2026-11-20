# EMA Hourly Continuation — P2P/USDT P21_50

**Symbol:** P2P/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 920 |
| net_profit_factor | 0.3348 |
| net_win_rate | 0.3380 |
| gross_profit_factor | 0.5325 |
| gross_win_rate | 0.3391 |
| sharpe_ratio | -9.5140 |
| sortino_ratio | -4.0543 |
| max_drawdown | 0.9930 |
| cagr | -0.8614 |
| net_avg_win | 16.0671 |
| net_avg_loss | -24.5105 |
| avg_hold_time_bars | 5.6185 |
| exposure | 0.2350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

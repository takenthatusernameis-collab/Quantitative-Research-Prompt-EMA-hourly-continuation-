# EMA Hourly Continuation — P2P/USDT P20_50

**Symbol:** P2P/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 919 |
| net_profit_factor | 0.3298 |
| net_win_rate | 0.3373 |
| gross_profit_factor | 0.5277 |
| gross_win_rate | 0.3384 |
| sharpe_ratio | -9.5016 |
| sortino_ratio | -4.0447 |
| max_drawdown | 0.9930 |
| cagr | -0.8610 |
| net_avg_win | 15.7644 |
| net_avg_loss | -24.3293 |
| avg_hold_time_bars | 5.8335 |
| exposure | 0.2437 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

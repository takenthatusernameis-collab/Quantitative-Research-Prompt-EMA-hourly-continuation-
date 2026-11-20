# EMA Hourly Continuation — P2P/USDT P21_100

**Symbol:** P2P/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.5049 |
| net_win_rate | 0.4006 |
| gross_profit_factor | 0.6584 |
| gross_win_rate | 0.4006 |
| sharpe_ratio | -5.0602 |
| sortino_ratio | -1.8015 |
| max_drawdown | 0.8827 |
| cagr | -0.5732 |
| net_avg_win | 34.8697 |
| net_avg_loss | -46.1594 |
| avg_hold_time_bars | 13.3012 |
| exposure | 0.3894 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

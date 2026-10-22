# EMA Hourly Continuation — XAI/USDT P144_200

**Symbol:** XAI/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 215 |
| net_profit_factor | 0.8064 |
| net_win_rate | 0.5163 |
| gross_profit_factor | 1.0584 |
| gross_win_rate | 0.5163 |
| sharpe_ratio | -0.9691 |
| sortino_ratio | -0.2045 |
| max_drawdown | 0.2553 |
| cagr | -0.0902 |
| net_avg_win | 79.2494 |
| net_avg_loss | -104.8925 |
| avg_hold_time_bars | 7.0651 |
| exposure | 0.0690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — XPR/USDT P20_89

**Symbol:** XPR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.7213 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.9138 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -2.1814 |
| sortino_ratio | -0.6230 |
| max_drawdown | 0.5371 |
| cagr | -0.2496 |
| net_avg_win | 69.6096 |
| net_avg_loss | -87.3590 |
| avg_hold_time_bars | 16.2612 |
| exposure | 0.2971 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

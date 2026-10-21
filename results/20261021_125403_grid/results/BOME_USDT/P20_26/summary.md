# EMA Hourly Continuation — BOME/USDT P20_26

**Symbol:** BOME/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 182 |
| net_profit_factor | 0.8067 |
| net_win_rate | 0.5165 |
| gross_profit_factor | 1.0594 |
| gross_win_rate | 0.5165 |
| sharpe_ratio | -0.8863 |
| sortino_ratio | -0.1721 |
| max_drawdown | 0.2699 |
| cagr | -0.0766 |
| net_avg_win | 80.5654 |
| net_avg_loss | -106.6732 |
| avg_hold_time_bars | 4.2802 |
| exposure | 0.0354 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

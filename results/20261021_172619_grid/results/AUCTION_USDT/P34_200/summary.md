# EMA Hourly Continuation — AUCTION/USDT P34_200

**Symbol:** AUCTION/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.7354 |
| net_win_rate | 0.4886 |
| gross_profit_factor | 0.9816 |
| gross_win_rate | 0.4914 |
| sharpe_ratio | -1.9994 |
| sortino_ratio | -0.5254 |
| max_drawdown | 0.5105 |
| cagr | -0.2213 |
| net_avg_win | 76.0420 |
| net_avg_loss | -98.7813 |
| avg_hold_time_bars | 31.1257 |
| exposure | 0.4931 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

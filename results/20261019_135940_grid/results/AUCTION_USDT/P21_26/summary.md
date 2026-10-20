# EMA Hourly Continuation — AUCTION/USDT P21_26

**Symbol:** AUCTION/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1131 |
| net_profit_factor | 0.2221 |
| net_win_rate | 0.3439 |
| gross_profit_factor | 0.6628 |
| gross_win_rate | 0.4173 |
| sharpe_ratio | -14.3058 |
| sortino_ratio | -7.0022 |
| max_drawdown | 0.9999 |
| cagr | -0.9761 |
| net_avg_win | 7.3391 |
| net_avg_loss | -17.3236 |
| avg_hold_time_bars | 2.8302 |
| exposure | 0.1449 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

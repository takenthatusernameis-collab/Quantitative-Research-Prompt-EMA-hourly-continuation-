# EMA Hourly Continuation — WAVES/USDT P12_34

**Symbol:** WAVES/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1440 |
| net_profit_factor | 0.4088 |
| net_win_rate | 0.4021 |
| gross_profit_factor | 0.9360 |
| gross_win_rate | 0.4417 |
| sharpe_ratio | -12.2420 |
| sortino_ratio | -6.5640 |
| max_drawdown | 0.9998 |
| cagr | -0.9655 |
| net_avg_win | 11.9406 |
| net_avg_loss | -19.6417 |
| avg_hold_time_bars | 3.9951 |
| exposure | 0.2615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

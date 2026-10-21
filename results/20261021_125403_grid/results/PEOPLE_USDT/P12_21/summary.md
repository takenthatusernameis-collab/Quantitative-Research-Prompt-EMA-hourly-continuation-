# EMA Hourly Continuation — PEOPLE/USDT P12_21

**Symbol:** PEOPLE/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.6685 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.9424 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -2.9211 |
| sortino_ratio | -0.8453 |
| max_drawdown | 0.6392 |
| cagr | -0.3206 |
| net_avg_win | 64.4169 |
| net_avg_loss | -86.9925 |
| avg_hold_time_bars | 4.9197 |
| exposure | 0.0915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

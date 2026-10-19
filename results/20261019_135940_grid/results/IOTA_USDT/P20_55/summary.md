# EMA Hourly Continuation — IOTA/USDT P20_55

**Symbol:** IOTA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 951 |
| net_profit_factor | 0.5282 |
| net_win_rate | 0.4490 |
| gross_profit_factor | 0.9852 |
| gross_win_rate | 0.4711 |
| sharpe_ratio | -7.0071 |
| sortino_ratio | -3.0421 |
| max_drawdown | 0.9782 |
| cagr | -0.7741 |
| net_avg_win | 25.5955 |
| net_avg_loss | -39.4861 |
| avg_hold_time_bars | 5.5910 |
| exposure | 0.2417 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

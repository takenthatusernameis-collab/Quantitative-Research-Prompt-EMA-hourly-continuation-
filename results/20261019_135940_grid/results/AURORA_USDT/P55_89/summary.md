# EMA Hourly Continuation — AURORA/USDT P55_89

**Symbol:** AURORA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 581 |
| net_profit_factor | 0.3969 |
| net_win_rate | 0.4028 |
| gross_profit_factor | 0.8183 |
| gross_win_rate | 0.4182 |
| sharpe_ratio | -7.6944 |
| sortino_ratio | -2.6121 |
| max_drawdown | 0.9684 |
| cagr | -0.7448 |
| net_avg_win | 27.2090 |
| net_avg_loss | -46.2330 |
| avg_hold_time_bars | 4.9432 |
| exposure | 0.1305 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

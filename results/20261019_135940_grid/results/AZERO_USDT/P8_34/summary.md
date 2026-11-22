# EMA Hourly Continuation — AZERO/USDT P8_34

**Symbol:** AZERO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1245 |
| net_profit_factor | 0.5116 |
| net_win_rate | 0.4514 |
| gross_profit_factor | 0.9622 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -7.2763 |
| sortino_ratio | -3.5696 |
| max_drawdown | 0.9885 |
| cagr | -0.8285 |
| net_avg_win | 18.4182 |
| net_avg_loss | -29.6250 |
| avg_hold_time_bars | 5.9133 |
| exposure | 0.3331 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — ZKJ/USDT P50_55

**Symbol:** ZKJ/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1076 |
| net_profit_factor | 0.1082 |
| net_win_rate | 0.2156 |
| gross_profit_factor | 0.4352 |
| gross_win_rate | 0.3522 |
| sharpe_ratio | -19.0587 |
| sortino_ratio | -9.9278 |
| max_drawdown | 1.0000 |
| cagr | -0.9956 |
| net_avg_win | 5.2290 |
| net_avg_loss | -13.2857 |
| avg_hold_time_bars | 2.5846 |
| exposure | 0.1264 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

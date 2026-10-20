# EMA Hourly Continuation — TNSR/USDT P26_144

**Symbol:** TNSR/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.6328 |
| net_win_rate | 0.4570 |
| gross_profit_factor | 0.8915 |
| gross_win_rate | 0.4685 |
| sharpe_ratio | -3.4929 |
| sortino_ratio | -1.1140 |
| max_drawdown | 0.7542 |
| cagr | -0.4147 |
| net_avg_win | 53.4259 |
| net_avg_loss | -71.0515 |
| avg_hold_time_bars | 20.0688 |
| exposure | 0.4750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

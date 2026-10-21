# EMA Hourly Continuation — BSV/USDT P12_200

**Symbol:** BSV/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.6583 |
| net_win_rate | 0.4468 |
| gross_profit_factor | 0.8060 |
| gross_win_rate | 0.4468 |
| sharpe_ratio | -2.3952 |
| sortino_ratio | -0.6141 |
| max_drawdown | 0.5251 |
| cagr | -0.2460 |
| net_avg_win | 66.5675 |
| net_avg_loss | -81.6697 |
| avg_hold_time_bars | 50.0912 |
| exposure | 0.7491 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

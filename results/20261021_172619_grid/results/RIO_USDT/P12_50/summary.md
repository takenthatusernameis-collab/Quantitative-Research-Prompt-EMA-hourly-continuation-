# EMA Hourly Continuation — RIO/USDT P12_50

**Symbol:** RIO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 592 |
| net_profit_factor | 0.8800 |
| net_win_rate | 0.5017 |
| gross_profit_factor | 1.0169 |
| gross_win_rate | 0.5017 |
| sharpe_ratio | -1.0691 |
| sortino_ratio | -0.3743 |
| max_drawdown | 0.4202 |
| cagr | -0.1627 |
| net_avg_win | 88.1555 |
| net_avg_loss | -100.8512 |
| avg_hold_time_bars | 10.4409 |
| exposure | 0.2838 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

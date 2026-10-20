# EMA Hourly Continuation — MANTA/USDT P100_144

**Symbol:** MANTA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.4631 |
| net_win_rate | 0.4416 |
| gross_profit_factor | 0.8189 |
| gross_win_rate | 0.4591 |
| sharpe_ratio | -5.1002 |
| sortino_ratio | -1.6433 |
| max_drawdown | 0.8650 |
| cagr | -0.5426 |
| net_avg_win | 32.6733 |
| net_avg_loss | -55.7991 |
| avg_hold_time_bars | 4.3560 |
| exposure | 0.1018 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — PYTH/USDT P100_144

**Symbol:** PYTH/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.4262 |
| net_win_rate | 0.4479 |
| gross_profit_factor | 0.7686 |
| gross_win_rate | 0.4556 |
| sharpe_ratio | -5.1868 |
| sortino_ratio | -1.6734 |
| max_drawdown | 0.8706 |
| cagr | -0.5558 |
| net_avg_win | 27.8428 |
| net_avg_loss | -52.9949 |
| avg_hold_time_bars | 3.8591 |
| exposure | 0.0909 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

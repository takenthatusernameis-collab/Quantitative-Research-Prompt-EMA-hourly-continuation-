# EMA Hourly Continuation — TRX/USDT P34_50

**Symbol:** TRX/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 761 |
| net_profit_factor | 0.1062 |
| net_win_rate | 0.2589 |
| gross_profit_factor | 0.7825 |
| gross_win_rate | 0.4336 |
| sharpe_ratio | -15.5503 |
| sortino_ratio | -6.9808 |
| max_drawdown | 0.9999 |
| cagr | -0.9782 |
| net_avg_win | 6.0299 |
| net_avg_loss | -19.8355 |
| avg_hold_time_bars | 3.0460 |
| exposure | 0.1054 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

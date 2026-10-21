# EMA Hourly Continuation — CELO/USDT P12_144

**Symbol:** CELO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.8911 |
| net_win_rate | 0.5147 |
| gross_profit_factor | 1.0688 |
| gross_win_rate | 0.5147 |
| sharpe_ratio | -0.7483 |
| sortino_ratio | -0.2070 |
| max_drawdown | 0.3760 |
| cagr | -0.0940 |
| net_avg_win | 93.9618 |
| net_avg_loss | -111.8564 |
| avg_hold_time_bars | 40.4745 |
| exposure | 0.6832 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

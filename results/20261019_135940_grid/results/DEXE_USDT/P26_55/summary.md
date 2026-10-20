# EMA Hourly Continuation — DEXE/USDT P26_55

**Symbol:** DEXE/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 910 |
| net_profit_factor | 0.3830 |
| net_win_rate | 0.4132 |
| gross_profit_factor | 0.7420 |
| gross_win_rate | 0.4319 |
| sharpe_ratio | -8.4227 |
| sortino_ratio | -3.5891 |
| max_drawdown | 0.9884 |
| cagr | -0.8301 |
| net_avg_win | 16.3184 |
| net_avg_loss | -29.9984 |
| avg_hold_time_bars | 6.8615 |
| exposure | 0.2838 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

# EMA Hourly Continuation — NEO/USDT P12_144

**Symbol:** NEO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.8213 |
| net_win_rate | 0.5062 |
| gross_profit_factor | 1.0135 |
| gross_win_rate | 0.5062 |
| sharpe_ratio | -1.0327 |
| sortino_ratio | -0.2664 |
| max_drawdown | 0.3152 |
| cagr | -0.1167 |
| net_avg_win | 75.0434 |
| net_avg_loss | -93.6583 |
| avg_hold_time_bars | 46.6512 |
| exposure | 0.6870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

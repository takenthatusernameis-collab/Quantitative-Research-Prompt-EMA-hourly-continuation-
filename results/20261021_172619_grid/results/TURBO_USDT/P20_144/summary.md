# EMA Hourly Continuation — TURBO/USDT P20_144

**Symbol:** TURBO/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.8101 |
| net_win_rate | 0.4866 |
| gross_profit_factor | 0.9540 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -1.4618 |
| sortino_ratio | -0.4172 |
| max_drawdown | 0.4315 |
| cagr | -0.1765 |
| net_avg_win | 87.4159 |
| net_avg_loss | -102.2572 |
| avg_hold_time_bars | 28.6269 |
| exposure | 0.5232 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

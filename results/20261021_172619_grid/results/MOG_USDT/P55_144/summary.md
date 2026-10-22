# EMA Hourly Continuation — MOG/USDT P55_144

**Symbol:** MOG/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.7671 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 0.9089 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -1.5256 |
| sortino_ratio | -0.4036 |
| max_drawdown | 0.4206 |
| cagr | -0.1698 |
| net_avg_win | 75.3452 |
| net_avg_loss | -91.0336 |
| avg_hold_time_bars | 13.6456 |
| exposure | 0.2144 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

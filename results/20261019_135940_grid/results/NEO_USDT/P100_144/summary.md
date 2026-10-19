# EMA Hourly Continuation — NEO/USDT P100_144

**Symbol:** NEO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.3675 |
| net_win_rate | 0.4239 |
| gross_profit_factor | 0.7887 |
| gross_win_rate | 0.4459 |
| sharpe_ratio | -6.9477 |
| sortino_ratio | -2.3097 |
| max_drawdown | 0.9449 |
| cagr | -0.6836 |
| net_avg_win | 23.7506 |
| net_avg_loss | -47.5502 |
| avg_hold_time_bars | 3.7376 |
| exposure | 0.0926 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

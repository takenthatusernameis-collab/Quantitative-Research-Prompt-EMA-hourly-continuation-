# EMA Hourly Continuation — NEO/USDT P34_100

**Symbol:** NEO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.6548 |
| net_win_rate | 0.4816 |
| gross_profit_factor | 0.9000 |
| gross_win_rate | 0.4816 |
| sharpe_ratio | -2.5420 |
| sortino_ratio | -0.7573 |
| max_drawdown | 0.6062 |
| cagr | -0.2922 |
| net_avg_win | 52.6467 |
| net_avg_loss | -74.6890 |
| avg_hold_time_bars | 13.7834 |
| exposure | 0.2719 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

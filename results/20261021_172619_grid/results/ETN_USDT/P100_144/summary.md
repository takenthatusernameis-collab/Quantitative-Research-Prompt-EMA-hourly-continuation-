# EMA Hourly Continuation — ETN/USDT P100_144

**Symbol:** ETN/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 194 |
| net_profit_factor | 0.5190 |
| net_win_rate | 0.4175 |
| gross_profit_factor | 0.6836 |
| gross_win_rate | 0.4175 |
| sharpe_ratio | -2.8940 |
| sortino_ratio | -0.6243 |
| max_drawdown | 0.4959 |
| cagr | -0.2507 |
| net_avg_win | 60.5693 |
| net_avg_loss | -83.6597 |
| avg_hold_time_bars | 6.5567 |
| exposure | 0.0691 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

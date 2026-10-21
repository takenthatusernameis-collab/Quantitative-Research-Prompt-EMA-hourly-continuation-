# EMA Hourly Continuation — TAO/USDT P20_100

**Symbol:** TAO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.9069 |
| net_win_rate | 0.5176 |
| gross_profit_factor | 1.0684 |
| gross_win_rate | 0.5176 |
| sharpe_ratio | -0.6495 |
| sortino_ratio | -0.1990 |
| max_drawdown | 0.3072 |
| cagr | -0.0922 |
| net_avg_win | 89.4246 |
| net_avg_loss | -105.8057 |
| avg_hold_time_bars | 18.3238 |
| exposure | 0.3781 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

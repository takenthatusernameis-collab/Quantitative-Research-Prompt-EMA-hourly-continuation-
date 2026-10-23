# EMA Hourly Continuation — ZKJ/USDT P21_144

**Symbol:** ZKJ/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 260 |
| net_profit_factor | 0.2324 |
| net_win_rate | 0.3154 |
| gross_profit_factor | 0.5703 |
| gross_win_rate | 0.3808 |
| sharpe_ratio | -6.8498 |
| sortino_ratio | -1.6196 |
| max_drawdown | 0.8855 |
| cagr | -0.5721 |
| net_avg_win | 32.5397 |
| net_avg_loss | -64.5055 |
| avg_hold_time_bars | 71.2115 |
| exposure | 0.8416 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

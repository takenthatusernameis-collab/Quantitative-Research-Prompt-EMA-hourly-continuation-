# EMA Hourly Continuation — KNC/USDT P34_144

**Symbol:** KNC/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.6844 |
| net_win_rate | 0.5023 |
| gross_profit_factor | 1.0536 |
| gross_win_rate | 0.5138 |
| sharpe_ratio | -2.5510 |
| sortino_ratio | -0.7443 |
| max_drawdown | 0.6193 |
| cagr | -0.3020 |
| net_avg_win | 59.1593 |
| net_avg_loss | -87.2378 |
| avg_hold_time_bars | 21.9585 |
| exposure | 0.4332 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

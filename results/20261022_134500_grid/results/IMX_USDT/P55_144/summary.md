# EMA Hourly Continuation — IMX/USDT P55_144

**Symbol:** IMX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.5762 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.8719 |
| gross_win_rate | 0.4822 |
| sharpe_ratio | -3.4314 |
| sortino_ratio | -1.0808 |
| max_drawdown | 0.7446 |
| cagr | -0.4074 |
| net_avg_win | 41.1750 |
| net_avg_loss | -65.5014 |
| avg_hold_time_bars | 10.6858 |
| exposure | 0.2447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.

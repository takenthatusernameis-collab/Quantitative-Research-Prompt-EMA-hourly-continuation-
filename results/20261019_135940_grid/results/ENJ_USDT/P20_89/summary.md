# EMA Hourly Continuation — ENJ/USDT P20_89

**Symbol:** ENJ/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 721 |
| net_profit_factor | 0.6060 |
| net_win_rate | 0.4577 |
| gross_profit_factor | 0.9537 |
| gross_win_rate | 0.4730 |
| sharpe_ratio | -4.8851 |
| sortino_ratio | -1.8416 |
| max_drawdown | 0.8988 |
| cagr | -0.5868 |
| net_avg_win | 41.5941 |
| net_avg_loss | -57.9295 |
| avg_hold_time_bars | 12.1040 |
| exposure | 0.3949 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
